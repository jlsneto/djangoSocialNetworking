from django.db import models

# Create your models here.
class Perfil(models.Model):

	nome = models.CharField(max_length=255, null=False)
	email = models.CharField(max_length=255, null=False)
	telefone = models.CharField(max_length=15, null=False)
	nome_empresa = models.CharField(max_length=255, null=False)
	contatos = models.ManyToManyField('self')

	#não confundir com a função convidar criada em views
	def convidar(self, perfil_convidado):
		convite = Convite(solicitante=self, convidado=perfil_convidado)
		convite.save()

class Convite(models.Model):
	#ler documentação backwards-related-objects. O django acaba criando uma coluna no banco para guardar todas as solicitações e convites recebidos
	solicitante = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='solicitacoes_enviadas')
	convidado = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='convites_recebidos')

	def aceitar(self):
		self.convidado.contatos.add(self.solicitante)
		self.solicitante.contatos.add(self.convidado)
		self.delete()
