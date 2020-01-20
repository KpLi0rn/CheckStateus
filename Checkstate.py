from urllib import request
import multiprocessing

"""
目的：通过筛选和排查 sublist3r 子域名爆破出来之后 
有些url无法进行访问，然后通过判断http的状态码进行一个筛选 
"""

def Read_domains(value):
    try:
        target = request.urlopen(url=value,timeout=3)
        page_stat = target.getcode()
        print(str(value) +" : " +  str(page_stat))
    except:
        pass

if __name__ == '__main__':
    path = input("please enter the path:").strip(' ')
    with open(path,'r') as file:
        for value in file.readlines():
            value = value.strip('\n').strip(',').strip('\'')
            value = "http://" + value
            p = multiprocessing.Process(target=Read_domains,args=(value,))
            p.start()
