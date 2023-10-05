import numpy as np


def game_core_v3(number: int = 1) -> int:
    
    '''
    Функция бинарного поиска: каждый раз отбрасывает "хвост" из значений, заведомо больше или меньше загаданного числа, 
    после чего запускает рекурсию на проверку из оставшихся значений
    '''
    def pred(count, bord_left, bord_right):
        count += 1
        
        predict_number = np.random.randint(bord_left, bord_right)
        
        if predict_number > number:
            return pred(count, bord_left, predict_number)
            
        elif predict_number < number:
            return pred(count, predict_number + 1, bord_right)
        
        else:
            return count
    
    return pred(0, 1, 101)


def score_game(random_predict) -> int:
    count_ls = []
    np.random.seed(1)  
    
    random_array = np.random.randint(1, 101, size=(10000))

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Мой алгоритм угадывает число в среднем за {score} попыток")


print('Run benchmarking for game_core_v3: ', end='')
score_game(game_core_v3)
