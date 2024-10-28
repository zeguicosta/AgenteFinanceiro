from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# Uncomment the following line to use an example of a custom tool
from analista_financeiro.tools.custom_tool import AnaliseFinanceira

# Check our tools documentations for more information on how to use them
from crewai_tools import SerperDevTool

@CrewBase
class AnalistaFinanceiroCrew():
	"""AnalistaFinanceiro crew"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def analista_precos(self) -> Agent:
		return Agent(
			config=self.agents_config['analista_precos'],
			tools=[AnaliseFinanceira(result_as_answer=True)], # Example of custom tool, loaded on the beginning of file
			verbose=True
		)

	@agent
	def analista_noticias(self) -> Agent:
		return Agent(
			config=self.agents_config['analista_noticias'],
			tools=[SerperDevTool()],
			verbose=True
		)
	
	@agent
	def escritor_relatorio(self) -> Agent:
		return Agent(
			config=self.agents_config['escritor_relatorio'],
			verbose=True
		)

	@task
	def obter_preco(self) -> Task:
		return Task(
			config=self.tasks_config['obter_preco'],
			agent=self.analista_precos(),
			output_file='analise.md'
		)

	@task
	def obter_noticias(self) -> Task:
		return Task(
			config=self.tasks_config['obter_noticias'],
			agent=self.analista_noticias(),
			output_file='noticias.md'
		)
	
	@task
	def escrever_relatorio(self) -> Task:
		return Task(
			config=self.tasks_config['escrever_relatorio'],
			agent=self.escritor_relatorio(),
			context=[self.obter_preco(), self.obter_noticias()],
			output_file='relatorio.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the AnalistaFinanceiro crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)