nums = [1, 2, 3] #criando uma lista com 3 elementos 
print(type(nums)) #<class 'list'>

nums.append(3) #adicionando o valor 3 ao final da lista
nums.append(4) #adicionando o valor 4 ao final da lista 
nums.append(500) #adicionando o valor 500 ao final da lista
print(len(nums)) #imprimindo o tamanho da lista 

nums[3] = 100 #alterando o valor do índice 3 da lista
nums.insert(0, -200) #adicionando o valor -200 no índice 0 da lista 

print(nums[6]) #imprimindo o valor do índice 6 da lista 
print(nums[-1])  #imprimindo o último valor da lista  
print(nums[-2]) #imprimindo o penúltimo valor da lista   
print(nums) #imprimindo a lista completa 