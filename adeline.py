def calcErrorValue(x_values, y_value, enter_weights):  

    z = sum([a*b for a,b in zip(enter_weights, x_values)])
    error = (y_value - z)

    return error



def learnModel(values_list, enter_weights, learning_coefficient, error_threshhold, print_weights = True):
    errors_exist = True
    epochs = 0
    
    while errors_exist:
        mean_square_sum = 0
        epochs += 1
        errors_exist = False

        for values in values_list:
            x_values = [-1 if x == 0 else x for x in values[0]]
            y_value = -1 if values[1] == 0 else values[1]

            error = calcErrorValue(x_values, y_value, enter_weights)
            for i in range(len(enter_weights)):
                enter_weights[i] += 2*(learning_coefficient * error * x_values[i])
            mean_square_sum += error**2   


        # Jeżeli wartość jest powyżej progu to aktualizujemy wektor wag
        mean_square = mean_square_sum / len(values_list)
        
        if(mean_square > error_threshhold):
            errors_exist = True
             

        if print_weights:
            print(enter_weights)
            print('mean_square_value: '+ str(mean_square))
    


    return enter_weights, epochs

    



def andFunc(value):
    if(value >= 0):
        return 1
    else:
        return -1