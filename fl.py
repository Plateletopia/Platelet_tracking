from IPython.display import clear_output  


class IvmObjects:
    def __init__(self,df_var_list):#, conf
        self.cols = col_list = [item for sublist in df_var_list for item in sublist]
        #self.inspect_steps = {}
#---------------------------------------------------------------------------------------------        
        
        
    def build_df_lists(df_var_list):
#for cat_names in dic_names:
#for name,dic in zip(dic_names,dic_list):
#    dic_names
    from IPython.display import clear_output    
    clear_output(wait=False)

    df_=[]
#df_cols=['pid', 'path', 'inh',]
    df_cols=[]
    for col_list,col_dict in zip(df_var_list,dic_list):
    #print(col_list,col_dict,'******')
    #print(col_dict[col_list[0]])
        for n in (col_list):
        #print(col_dict[n])
            try:
                df_cols.append(col_dict[n])
            except:    
                print('something wrong with indata')
    arr_txt = [x for x in os.listdir() if x.endswith("dataframe")]
    for c, value in enumerate(arr_txt,0):
        print(c, value) 
    col_vars=input("Choose the dataframes you want to use separeted by spaces from the list below:")
    #print("Enter your choice as integers separeted by spaces: ")
    flist = [int(x) for x in col_vars.split()]
    
    
    #print(f'Including columns:{df_cols}')
    #clear_output(wait=False)
    for n_df,fi in enumerate(flist):
        dfi=pd.read_pickle(arr_txt[fi])
        dfi_col=['pid', 'path', 'inh',]
        for col in df_cols:
            if col in dfi.columns:
                dfi_col.append(col)      
        df_.append(dfi.loc[:,dfi_col])
    pc=pd.concat(df_, ignore_index=True,names='pid').reset_index()
    pc.index.name = 'pid'
    
    if 'nrtracks' in pc:
        choice = input('Do you only want to analyze tracked plts? (y/n)')
        if choice =='y':
            print('Set tracking threshold as integer')
            thr_tr=int(input())
            pc=pc[pc.nrtracks>thr_tr]
    #clear_output(wait=False)
    print(f'RESULTING DATAFRAME\nNo of columns: {pc.shape[1]} \nNo of rows: {pc.shape[0]}',
          f'\nMemory use: {np.round(sys.getsizeof(pc)/1000000,1)} Mb')
    
#---------------------------------------------------------------------------------------------        

        
#class imfiles:

 #   def __init__(self, root_path):
 #       self.root_path=root_path
 #       self.fpos_inh=3
  #      self.fpos_inj=2
   #     self.fpos_type=4
    #    self.fpos_date=0
    #    self.fpos_mouse=1##