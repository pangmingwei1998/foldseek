# -*- coding: utf-8 -*-
import os
print(os.getcwd())
# 存放要批量查找的pdb文件的路径
pdb_ls = os.listdir('./pdb_structures')

for pdbfile in pdb_ls:
    inp = './pdb_structures/' + pdbfile
    # 构建输出文件的路径
    oup = './align_out/' + pdbfile[0:-3] + '_aln'
    # 构建要执行的命令字符串
    cmd = 'foldseek easy-search ' + inp + ' pdb ' + oup + ' tmp --format-output query,target,fident,alnlen,mismatch,gapopen,qstart,qend,tstart,tend,evalue,bits,prob,lddt,alntmscore'
    print(cmd)
    os.system(cmd)

# #查看内容
# import pandas as pd
# col_names = 'query,target,fident,alnlen,mismatch,gapopen,qstart,qend,tstart,tend,evalue,bits,prob,lddt,alntmscore'.split(',')
# df_aln = pd.read_table('./align_out/蛋白名字._aln',names=col_names)
# print(df_aln)