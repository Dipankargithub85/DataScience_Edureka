
def calculation(n):
    sum=0.0
    for i in range(1,n+1):
        sum += float(float(i)/(i+1))

    format_float = "{:.2f}".format(sum)
    print("The output of the program is:")
    print(format_float)


if __name__ == '__main__':
    n = int(input("Enter the limit:"))
    calculation(n)