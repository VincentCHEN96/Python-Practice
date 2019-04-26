def make_car(manufacturer, model, **others):
    car_info = {'manufacturer':manufacturer, 'model':model}
    if others:
        for key, value in others.items():
            car_info[key] = value
    return car_info


car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)