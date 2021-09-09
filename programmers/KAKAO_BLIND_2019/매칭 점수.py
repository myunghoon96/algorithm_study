#https://programmers.co.kr/learn/courses/30/lessons/42893

import re
#여행 #게임 #낚시 #
def solution(word, pages):
    answer = 0
    url_info = dict()
    connect_dict = dict()
    for page in pages:

        my_url = re.search('<meta property="og:url" content="https://([\S]*)"/>', page).group(1)
        href_url = re.findall('<a href="https://([\S]*)">', page)
        
        base_score = 0
        query_candidate = re.findall('[a-zA-Z]*', page.lower())
        for candidate in query_candidate:
            if word.lower() == candidate:
                base_score+=1
        
        url_info[my_url] = (base_score, href_url)
        
        for href in href_url :
            if connect_dict.get(href) != None:
                connect_dict[href].append(my_url)
            else:
                connect_dict[href]=[]
                connect_dict[href].append(my_url)
    # print(connect_dict)
    
    max_score = -1
    max_index = -1
    for i, (my_url, (base_score, href_url)) in enumerate(url_info.items()):
        # print(i, my_url, base_score, href_url)
        href_score = 0
        
        if connect_dict.get(my_url) != None:
            for c_url in connect_dict[my_url]:
                if url_info.get(c_url) != None and len(url_info[c_url][1]) != 0:
                    href_score += url_info[c_url][0] / len(url_info[c_url][1])

        if max_score < href_score+base_score:
            max_score = href_score+base_score
            max_index = i
        # print(i, my_url, href_score+base_score)
    return max_index