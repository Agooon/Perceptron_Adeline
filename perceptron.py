
def calcValue(enter_values, enter_weights):
    sum = 0
    for i in range(len(enter_values)):
        sum+= enter_values[i] * enter_weights[i]
    return sum

def andFunc(value, threshold, unipolar = False):
    if(value > threshold):
        return 1
    else:
        if(unipolar):
            return -1
        return 0

def learnModel(values_list, enter_weights, learning_coefficient, threshold, print_weights = True, unipolar = False):
    errors_exist = True
    epochs = 0

    while errors_exist:
        errors_exist = False
        epochs += 1

        for values in values_list:
            result = calcValue(values[0], enter_weights)
            error = values[1] - andFunc(result, threshold, unipolar)
            # Jeżeli jakaś z wartości nie spełnia warunku to poprawiamy wagi oraz dokonamy jeszcze jednej iteracji
            if(error != 0 ):
                errors_exist = True
                for i in range(len(enter_weights)):
                    enter_weights[i] = enter_weights[i] + learning_coefficient * error * values[0][i]

        if print_weights:
            print(enter_weights)


    return enter_weights, epochs
