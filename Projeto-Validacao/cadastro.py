from datetime import datetime, timedelta


class Cadastro:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.format_data(self.momento_cadastro)

    def mes_cadastro(self):
        meses_do_ano = [
            "", "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
            "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
        ]
        mes_cadastro = self.momento_cadastro.month
        return meses_do_ano[mes_cadastro]

    def dia_cadastro(self):
        dias_da_semana = [
            "", "segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo"
        ]
        dia_semana = self.momento_cadastro.weekday()
        return dias_da_semana[dia_semana]

    def format_data(self, data):
        data_formatada = data.strftime("%d/%m/%Y %H:%M")
        return data_formatada

    def data_atualizar_cadastro(self):
        data_atualizar_cadastro = datetime.today() + timedelta(days=60)
        return self.format_data(data_atualizar_cadastro)
