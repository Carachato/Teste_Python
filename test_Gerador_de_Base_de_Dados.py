import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
from Gerador_de_Base_de_Dados import (
    gerar_estados, gerar_canais_vendas, gerar_motivo_compra, gerar_produtos,
    gerar_valor_produtos, gerar_qtd_vendida, gerar_datas, gerar_faturamento
)

class TestGeradorBaseDeDados(unittest.TestCase):
    @patch('random.choices')
    def test_gerar_estados(self, mock_choices):
        mock_choices.return_value = ['SP', 'RJ']
        result = gerar_estados(2)
        self.assertEqual(result, ['SP', 'RJ'])
        mock_choices.assert_called_once()

    @patch('random.choices')
    def test_gerar_canais_vendas(self, mock_choices):
        mock_choices.return_value = ['Online', 'Loja Física']
        result = gerar_canais_vendas(2)
        self.assertEqual(result, ['Online', 'Loja Física'])
        mock_choices.assert_called_once()

    @patch('random.choices')
    def test_gerar_motivo_compra(self, mock_choices):
        mock_choices.return_value = ['Necessidade', 'Indicação']
        result = gerar_motivo_compra(2)
        self.assertEqual(result, ['Necessidade', 'Indicação'])
        mock_choices.assert_called_once()

    @patch('random.choices')
    def test_gerar_produtos(self, mock_choices):
        mock_choices.return_value = ['Produto A', 'Produto B']
        result = gerar_produtos(2)
        self.assertEqual(result, ['Produto A', 'Produto B'])
        mock_choices.assert_called_once()

    @patch('random.choices')
    def test_gerar_valor_produtos(self, mock_choices):
        mock_choices.return_value = [200, 300]
        result = gerar_valor_produtos(2)
        self.assertEqual(result, [200, 300])
        mock_choices.assert_called_once()

    @patch('random.choices')
    def test_gerar_qtd_vendida(self, mock_choices):
        mock_choices.return_value = [5, 10]
        result = gerar_qtd_vendida(2)
        self.assertEqual(result, [5, 10])
        mock_choices.assert_called_once()

    @patch('pandas.date_range')
    @patch('random.choices')
    def test_gerar_datas(self, mock_choices, mock_date_range):
        # Retorna um DatetimeIndex, que é compatível com .strftime()
        mock_date_range.return_value = pd.to_datetime(['2023-01-01', '2023-01-02'])
        mock_choices.return_value = ['01/01/2023', '02/01/2023']
        result = gerar_datas('01/01/2023', '02/01/2023', 2)
        self.assertEqual(result, ['01/01/2023', '02/01/2023'])
        mock_date_range.assert_called_once()
        mock_choices.assert_called_once()

    def test_gerar_faturamento(self):
        df = pd.DataFrame({
            'Valor do Produto': [10, 20],
            'Quantidade Vendida': [2, 3]
        })
        result = gerar_faturamento(df.copy())
        self.assertIn('Faturamento', result.columns)
        self.assertEqual(list(result['Faturamento']), [20, 60])

if __name__ == '__main__':
    unittest.main()
