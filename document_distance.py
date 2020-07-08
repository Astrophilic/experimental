import  sys
import math
def get_lines(filename):
    with open(filename) as f:
        lines = f.readlines()
        lines = [l.rstrip('\n') for l in lines]
        return lines


def get_words_from_lines(lines):
    word_list=[]
    current_word=[]
    for line in lines:
        for c in line:
            if c.isalnum():
                current_word.append(c)
            else:
                if len(current_word)>0:
                    word_list.append(''.join(current_word))
                    current_word=[]
    
    return word_list

def get_word_count_dict(words_list):
    L={}

    for word in words_list:
        if word in L:
            L[word]+=1
        else:
            L[word]=1
    return L

def get_frequency_vector(filename):
    lines_list = get_lines(filename)
    words_list =get_words_from_lines(lines_list)
    word_count_dict =get_word_count_dict(words_list)
    print(word_count_dict)

    print('\n')
    return word_count_dict


def inner_product(L1,L2):
    sum =0
    for key, value in L1.items():
        if key in L2:
            sum+=value*L2[key]
    print(sum)
    return sum
def vector_angle(L1,L2):
    numerator = inner_product(L1,L2)
    denominator = math.sqrt(inner_product(L1,L1)*inner_product(L2,L2))

    angle = math.acos(numerator/denominator)
    return angle
    


def main():
    if len(sys.argv) != 3:
        print('Please enter script source_filename target_filename in order')
    source_filename = sys.argv[1]
    target_filename = sys.argv[2]

    frequency_vector_source_file = get_frequency_vector(source_filename)
    frequency_vector_target_file = get_frequency_vector(target_filename)
   
    distance = vector_angle(frequency_vector_source_file,
    frequency_vector_target_file)

    print('The vector distance between 2 files is {}'.format(distance))


if __name__ == "__main__":
    main()