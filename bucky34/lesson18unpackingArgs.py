def health_calculator(age, apples, cigs_smoked):
    answer = (100-age) + (apples * 3.5) - (cigs_smoked * 2)
    print(answer)

javier_data = [33, 5, 0]

health_calculator(javier_data[0], javier_data[1], javier_data[2])
health_calculator(*javier_data)
