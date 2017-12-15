import asyncio
import os
import random
import command_execution
from command_execution import CommandResult



async def pdf_from_latex(latex:str, file_name_without_extention:str) -> CommandResult:
    file_name_base = file_name_without_extention
    tex_file_name = f'{file_name_base}.tex'

    with open(tex_file_name,'w') as f:
        f.write(latex)

    results = await command_execution.run_command_str(f'pdflatex {tex_file_name}')
    #remove temp files
    os.remove(tex_file_name)
    os.remove(f'{file_name_base}.aux')
    os.remove(f'{file_name_base}.log')
    return results






if __name__ == '__main__':
    id = random.randint(0, 1_000_000_000)
    id = 104156776
    random.seed(id)

    print('creating a latex addition worksheed (proof of concept code)')
    latex = r'''
        \documentclass{article}
        \usepackage{geometry}
            \geometry{
                a4paper,
                total={170mm,257mm},
                left=20mm,
                right=20mm,
                top=20mm,
                bottom=20mm
            }

        \usepackage{multicol}

        \setlength\parindent{0pt}

        \begin{document}
             \pagenumbering{gobble}
            Name: $\rule{10cm}{0.15mm}$ \\
            \begin{multicols}{3}
            \fontsize{0.3cm}{0.7cm}\selectfont'''+'\n'
    for question_number in range(1,100+1):
        #print(question_number)
        a = random.randint(0, 10)
        b = random.randint(0, 10)

        latex += f'\t\t\t{question_number}) ${a} + {b} = $' + r'$\rule{1cm}{0.15mm}$ \\'+'\n'


    latex += r'''
            $ 1 + 2 = $ \\
            $3 $ \\
            $ 1 + 2 =  = 3$ \\
            \end{multicols}
            \fontsize{0.1cm}{0.1cm}\selectfont
    '''
    latex += r'\vfill \hfill' + f'(worksheet id: {id})' + r'\\'
    latex += r'''
        \end{document}
    '''

    loop = asyncio.get_event_loop()
    results:CommandResult = loop.run_until_complete(pdf_from_latex(latex, f'Worksheet_{id}'))
    #command_execution.print_result(results)
