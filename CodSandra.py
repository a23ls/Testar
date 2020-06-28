#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 22:01:43 2020

@author: afflorezr
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 19:44:05 2020

@author: afflorezr
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 19:41:06 2020

@author: afflorezr
"""

#Import library essentials
#Import library essentials

import PyPDF2
from sumy.parsers.plaintext import PlaintextParser #We're choosing a plaintext parser here, other parsers available for HTML etc.
from sumy.nlp.tokenizers import Tokenizer 
from sumy.summarizers.lsa import LsaSummarizer #We're choosing Luhn, other algorithms are also built in
from sumy.summarizers.lex_rank import LexRankSummarizer


pdf_file = open('Tese Sandra.pdf', 'rb')
read_pdf = PyPDF2.PdfFileReader(pdf_file)
number_of_pages = read_pdf.getNumPages()
summaries=[]
summaries_Rank=[]



## segunda modificação
## pequena modificação