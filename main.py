import perceptron
from random import random
from random import uniform
import adeline
# Zmienne wysyłane do perceptrona
values_p = [[[0,0], 0], [[0,1], 0], [[1,0], 0], [[1,1], 1]]
values_p_extended = [[[1,0,0], 0], [[1,0,1], 0], [[1,1,0], 0], [[1,1,1], 1], [[1,0.9,0.8], 1] , [[1,0.96,0.97], 1]]
enter_weights_p = [0.1, 0.1]
learning_coefficient_p = 0.01
threshold_p = 1

# Zmienne wysyłane do adeline
values_a_b = [[[1,0,0], 0], [[1,0,1], 0], [[1,1,0], 0], [[1,1,1], 1]]
values_a_b_extended = [[[1,0,0], 0], [[1,0,1], 0], [[1,1,0], 0], [[1,1,1], 1], [[1,0.89,0.95], 1] , [[1,0.91,0.92], 1]]
enter_weights_a_b = [0.1, -0.2, 0.1]
learning_coefficient_a = 0.1
error_threshhold = 0.5

def threshold_test():
    learning_coefficient = 0.01
    enter_weights = [0.01, 0.01]
    values = [[[0,0], 0], [[0,1], 0], [[1,0], 0], [[1,1], 1]]
    print('threshold;epochs'  )
    for threshold in [ 0.1, 0.2, 0.5, 1, 2, 3, 5, 10, 20, 50, 100]:
        enter_weights = [0.01, 0.01]
        _, epochs = perceptron.learnModel(values, enter_weights, learning_coefficient, threshold, False)  
        print(str(threshold) +';'+ str(epochs))
        # print('weights:  ' + str(weights))

def random_weight_test():
    learning_coefficient = 0.01
    enter_weights = [0.01, 0.01]
    values = [[[0,0], 0], [[0,1], 0], [[1,0], 0], [[1,1], 1]]
    threshold = 1
    number_of_repeats = 10
    print('rand_range;epochs'  )
    for rand_range in [ [-1,1], [-0.8,0.8], [-0.5,0.5], [-0.3, 0.3], [-0.2, 0.2], [-0.1, 0.1]]:
        epochs_sum = 0
        for i in range(number_of_repeats):
            enter_weights = [uniform(rand_range[0], rand_range[1]), uniform(rand_range[0], rand_range[1])]
            _, epochs = perceptron.learnModel(values, enter_weights, learning_coefficient, threshold, False)
            epochs_sum += epochs  
        
        print(str(rand_range) +';'+ str(epochs_sum/number_of_repeats))

def learning_coefficient_test():
    values = [[[0,0], 0], [[0,1], 0], [[1,0], 0], [[1,1], 1]]
    threshold = 10 ## Tak aby dla 1 było możliwe znalezienie rozwiązania
    print('learning_coefficient;epochs'  )
    for learning_coefficient in [ 0.00001, 0.0001, 0.001, 0.01, 0.1, 0.2, 0.4, 0.7, 1]:
        enter_weights = [0.01, 0.01]
        _, epochs = perceptron.learnModel(values, enter_weights, learning_coefficient, threshold, False)  
        print(str(learning_coefficient) +';'+ str(epochs))
        # print('weights:  ' + str(weights))

def learning_function_test():
    values = [[[0,0], 0], [[0,1], 0], [[1,0], 0], [[1,1], 1]]
    learning_coefficient = 0.01
    threshold = 1

    print('Funkcja aktywacji;Liczba epok')
    enter_weights = [0.01, 0.01]
    _, epochs = perceptron.learnModel(values, enter_weights, learning_coefficient, threshold, False)
        
    print('unipolarna;'+ str(epochs))

    values = [[[-1,-1], -1], [[-1,1], -1], [[1,-1], -1], [[1,1], 1]]
    enter_weights = [0.01, 0.01]
    _, epochs = perceptron.learnModel(values, enter_weights, learning_coefficient, threshold, False, True)
        
    print('bipolarna;'+ str(epochs))

def random_weight_adeline_test():
    values_a_b = [[[1,0,0], 0], [[1,0,1], 0], [[1,1,0], 0], [[1,1,1], 1]]
    learning_coefficient = 0.01
    error_threshold = 0.55

    number_of_repeats = 100

    print('rand_range;epochs')

    for rand_range in [ [-1,1], [-0.8,0.8], [-0.5,0.5], [-0.3, 0.3], [-0.2, 0.2], [-0.1, 0.1]]:
        epochs_sum = 0
        for i in range(number_of_repeats):
            enter_weights = [uniform(rand_range[0], rand_range[1]), uniform(rand_range[0], rand_range[1]), uniform(rand_range[0], rand_range[1])]
            _, epochs = adeline.learnModel(values_a_b, enter_weights, learning_coefficient, error_threshold, False)
            epochs_sum += epochs  
        
        print(str(rand_range) +';'+ str(epochs_sum/number_of_repeats))

def learning_coefficient_adeline_test():
    values_a_b = [[[1,0,0], 0], [[1,0,1], 0], [[1,1,0], 0], [[1,1,1], 1]]
    error_threshold = 0.55

    print('learning_coefficient;epochs'  )
    for learning_coefficient in [ 0.00001, 0.0001, 0.001, 0.01, 0.1, 0.15, 0.2, 0.7, 1]:
        enter_weights = [0.1, 0.1, 0.1]
        _, epochs = adeline.learnModel(values_a_b, enter_weights, learning_coefficient, error_threshold, False)  
        print(str(learning_coefficient).replace('.',',') +';'+ str(epochs))
        # print('weights:  ' + str(weights))

def error_threshold_adeline_test():
    values_a_b = [[[1,0,0], 0], [[1,0,1], 0], [[1,1,0], 0], [[1,1,1], 1]]
    error_threshold = 0.55
    learning_coefficient = 0.0001

    print('error_threshold;epochs')
    for error_threshold in [ 1, 0.8, 0.5, 0.4, 0.35, 0.3, 0.29, 0.28, 0.27, 0.26, 0.255, 0.251]:
        enter_weights = [0.1, 0.1, 0.1]
        weights, epochs = adeline.learnModel(values_a_b, enter_weights, learning_coefficient, error_threshold, False)  
        print(str(error_threshold).replace('.',',') +';'+ str(epochs))
        # print('weights:  ' + str(weights))

if __name__ == '__main__':    
    #                      #
    ### Perceptron tests ###
    #                      #

    # threshold_test()

    # random_weight_test()

    # learning_coefficient_test()

    # learning_function_test()


    #                   #
    ### Adeline tests ###
    #                   #

    # random_weight_adeline_test()

    # Nie osiągamy wyników dla wartości większych od 0.1
    # learning_coefficient_adeline_test()


    error_threshold_adeline_test()
        