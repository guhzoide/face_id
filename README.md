# FACE_ID

#------------------------------------------------------------------------------------------------------------------------------#
	
	Autor:		Hugo Ferreira                                                       
	git-hub:	github.com/guhzoide                                                     

	Projeto da faculdade - Finalizado.
	
	Requisitos:
		Python 3.10.6
		pip 22.2.2
		Servidor Linux - ubuntu-server

	Como Executar:
		Execute o script prepare.sh dentro da pasta face_id
		
		Após criar o servidor jogue o script server.sh para o servidor e execute.

		Feito isso informe no aquivo info.py, informações como ip, user, pass, e-mail
		    para as conexões do servidor e banco.
			
		Com tudo finalizado basta executar o main.py
		
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

	Atualizações

	Atualização = 22/03/2022:
		Identificação de face atravez de um frame utilizando o OpenCV.
	
	Atualização = 08/04/2022:
		Implementado a biblioteca 'facepplib' e a verificação/liberação.
	
	Atualização = 19/04/2022:
		Adcionado o tratamento de multiplas faces impedindo de realizar a verificação/liberação 
		caso ouver mais de uma. 

	Atualização = 17/06/2022:
		conexão com servidor para salvar as imagens de cadastros e tentativas de acesso.

	Atualização = 27/07/2022:
		Adcionado a opção de atualizar o banco de castro local.

	Atualização = 15/08/2022:
		Adcionado a opção de visualizar tentativas de acesso tanto negado quanto autorizado.

	Atualização = 25/08/2022:
		Verificação será realizada sem precisar digitar o nome do colaborador
	
	Atualização = 26/08/2022:
		Ao realizar o cadastro será gerado um QRCode que irá ser utilizado na identificação.
		Adcionado a opção de visualizar o log de erros do sistema.

	Atualização = 14/09/2022:
		Troca de pacote para criação do QRCODE e melhora no tutorial presente no README.md
		Criação dos shell scripts para preparação da maquina e do servidor.

	Atualização = 13/10/2022:
		Melhoria no processo de identificação adcionando prova de vida para evitar o burlamento
		do sistema.
		
	Aualização = 21/10/2022:
		Alteração no design e melhoria na acessibilidade almentando fonts e organizando de forma
		mais agradavel os botões do menu.

	Atualização = 12/11/2022:
		Adcionado envio de e-mail com o QRCode em anexo.

	Atualização = 17/11/2022;
		Adcionado opção de reenviar QRCode de cadastro já exixtente. 

	Atualização = 06/03/2023;
		Adcionado opção de acadstro manual, sem a necessidade de estar presente no local, e também
		um sistema de nível de acesso.

	Atualização = 20/03/2023;
		Alterado as telas de reenvio de qrcode e atela de cadastro para um novo layout. Adcionado
		sistema de nível de cadastro na idenficação.

	Atualização = 24/04/2023;
		Alteração no porcesso de cadastro, substituido o qrcode por matricula.

	Atualização = 05/05/2023;
		Alterado banco de dados de local para banco em nuvem. 

#------------------------------------------------------------------------------------------------------------------------------#
