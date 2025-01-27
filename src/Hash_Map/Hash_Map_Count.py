def countHashdata(s):
    freq = {}
    for piece in s.lower().split():
        word  = ''.join(c for c in piece if c.isalpha())
        if word:
            freq[word] = 1 + freq.get(word,0)

    max_word = ''
    max_count = 0
    for (w,c) in freq.items():
        if c > max_count:
            max_count = c 
            max_word = w

    print('Palavra mais frequente: ', max_word)
    print('Maximo de ocorrencia: ', max_count)

countHashdata(
    '''
    Na faculdade, na aula de História da Arte, o professor tornou obrigatória a leitura de Maus de Art Spiegelman.

Eu não li durante o curso, porque entre o grande volume de coisas, acabei o sacrificando. Não lembro muito bem o porquê, talvez porque fosse um dos mais grossos e basicamente esse era o meu filtro.

Foi recém-formada que encontrei a história perdida entre tantos xerox.

Li um pequeno trecho e depois o procurei nas livrarias.

Maus ("rato", em alemão) conta a história de um judeu polonês que sobreviveu ao campo de concentração de Auschwitz, narrada por seu filho Art em quadrinhos. E enquanto Art narra a experiência do seu pai, ele também aborda a relação entre eles. Super recomendo.
    '''
)