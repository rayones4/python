mat1=[[2,3,0],[5,6,1],[8,2,3]]
mat2=[[0,5,8],[1,5,9],[8,6,7]]
mat3=[[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(mat1)):
    for j in range(len(mat1[0])):
        mat3[i][j]=mat1[i][j] + mat2[i][j]
    print(mat3)