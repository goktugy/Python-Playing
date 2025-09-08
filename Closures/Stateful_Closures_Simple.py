def cumulative_average() -> object:
    data =[]
    def calculate_average(value):
        data.append(value)
        return sum(data) / len(data)
    return calculate_average

if  __name__ == '__main__':
    cum_average_calculator = cumulative_average()
    print(cum_average_calculator(10))
    print(cum_average_calculator(20))
    print(cum_average_calculator(30))
