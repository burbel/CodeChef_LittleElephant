#! /usr/bin/env python

def main():    # Don't leave the code in the global namespace, it runs slower
    import sys
    tokenizedInput = map(int, sys.stdin.read().split())

    K, N = tokenizedInput[0:2]
    lucky_list = []

    for count in xrange(K):
        lucky_list.append(str(tokenizedInput[2+count]))

    for count in xrange(N):
        test_string = str(tokenizedInput[2+K+count])
        output_string = "Bad"
        if len(test_string) >= 47:
            output_string =  "Good"
        for lucky_string in lucky_list:
            if (lucky_string in test_string):
                output_string = "Good"
        print output_string

main()
