count_box =int(input('vvedite kolithestvo yashikov'))
boxes = [i for i in range(1,count_box +1)]
container = 1
truck = 1
for box in boxes:
    print('------ящик '+ str(box))
    if container % 12 == 0 and box % 27 == 0:
        truck +=1
        print('--Грузовик '+ str(truck) + ":")
    if box % 27 == 0:
        container += 1
        print('----Контейнер '+ str(container) + ":")
print('end')
print("")
print(f'truck-{truck}, container-{container} , box-{box}')

