import math
import time

# primeira versão do algoritmo

def guess_number(): 
    print('Escolha um número entre 1 e 100...')
    time.sleep(3)
    biggest_number = 100
    smallest_number = 0
    half = 50
    try_counter = 0
    founded_number = False
    while not founded_number:
        try_counter += 1
        number_chosen = input(
            f'{try_counter} tentativa - O número escolhido foi {half}?\n'
            ' s - para sim\n'
            ' n - para não\n'
            )
        if number_chosen == 's':
            print('\neu falei que conseguiria...')
            break
        else:
            chosen_option = input(
            f'O número escolhido é maior que {half}?\n'
            ' s - para sim\n'
            ' n - para não\n'
            )
        if chosen_option == 's':
            smallest_number = half
            half = math.ceil((biggest_number + smallest_number) // 2)
            
        else:
            biggest_number = half
            half = math.ceil((biggest_number + smallest_number) // 2)
        


# versão utilizando a recursividade

def guess_number_v2(b_number = 100, s_number = 0, t_counter = 1, h = 50):
    biggest_number = b_number
    smallest_number = s_number
    half = h
    try_counter = t_counter
    number_chosen = input(
            f'{try_counter} tentativa - O número escolhido foi {half}?\n'
            ' s - para sim\n'
            ' n - para não\n'
            )
    if number_chosen == 's':
        print('\neu falei que conseguiria...')
        return None
    else:
        chosen_option = input(
            f'O número escolhido é maior que {half}?\n'
            ' s - para sim\n'
            ' n - para não\n'
            )
        if chosen_option == 's':
            guess_number_v2(
                biggest_number, 
                half, 
                try_counter + 1, 
                math.ceil((biggest_number + half) // 2)
                )

            
        else:
            guess_number_v2(
                half, 
                smallest_number, 
                try_counter + 1, 
                math.ceil((half + smallest_number) // 2)
                )
            


if __name__ == '__main__':
    # guess_number()
    guess_number_v2()