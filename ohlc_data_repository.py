/************************************************************************
*																		*
* "Ramlogics Metatrader" is a script developed by Ramlogics Technosoft. *
*		   All right reserved by Ramlogics Technosoft Pvt. Ltd. 		*
*																		*
*    Copyright (C) 2022 Ramlogics Technosoft.  All rights reserved.	    *
*																		*
************************************************************************/

from core.symbol_tf import SymbolTF
from core.ohlc_data import OhlcData

class OhlcDataRepository:
    def __init__(self):
        pass

    def load_by_symbol_and_df(self, symbol_tf, start_index, qtd):
        if not isintance(symbol_tf, SymbolTF):
            return False
        pass