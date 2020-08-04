"""
    Módulo notafiscal -
    Classe NotaFiscal - 
        Atributos :
            id        - informado.
            codigo    - informado.
            data      - informado.
            cliente   - informado.
            items     - informado
            valornota - calculado. 
"""
import datetime
from cliente        import Cliente
from produto        import Produto
from itemnotafiscal import ItemNotaFiscal


class NotaFiscal():         
    def __init__(self, Id, codigo, cliente):
        self._Id = Id
        self._codigo=codigo
        self._cliente=cliente 
        self._data=datetime.datetime.now()   
        self._itens=[]
        self._valorNota=0.0        
        
    def setCliente(self, cliente):
        if isinstance(cliente, Cliente):
            self._cliente=cliente    
            
    def adicionarItem(self, item): 
        if isinstance(item, ItemNotaFiscal):
            self._itens.append(item)
        
    def calcularNotaFiscal(self):
        valor=0.0
        for item in self._itens:
            valor =+ item._valorItem
        self.valorNota=valor
        
    def imprimirNotaFiscal(self):
        print('-' * 82)
        print('NOTA FISCAl',' ' * 57 ,self._data.year,'/',self._data.month,'/',self._data.day)
        print('Cliente: ', self._cliente._codigo,'  ', 'Nome:', self._cliente._nome)
        print('CPF/CNPJ: ', self._cliente._cnpjcpf)
        print('-' * 82)

        print('ITENS')
        print('-' * 82)
        print('Seq', ' ' * 2, 'Descrição', ' ' * 15, 'QTD', ' ' * 4, 'Valor Unit', ' ' * 4, 'Preço')
        print('-' * 3, ' ' * 2, '-' * 22, ' ' * 2, '-' * 3, ' ' * 4, '-' * 10, ' ' * 4, '-' * 5)
        
        for item in self._itens:
            print(item._sequencial, ' ' * 4, 
            item._descricao, ' ' * 13, 
            item._quantidade, ' ' * 7, 
            item._valorUnitario, ' ' * 7, 
            item._valorItem)
        
        print('_' * 82)
        print('Valor total: ', self._valorNota)
    
    
        
        