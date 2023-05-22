setwd("C:/Users/kdtorres/Documents/Programacao/PI_IV/previsaodetemperaturasporseriestemporais")
getwd()

library(readr)
dados_A701_H_2006_07_24_2023_03_22 <- read_delim("dados_A701_H_2006-07-24_2023-03-22.csv", 
                                                 delim = ";", escape_double = FALSE, na = "null", 
                                                 trim_ws = TRUE, skip = 9)
View(dados_A701_H_2006_07_24_2023_03_22)
summary(dados_A701_H_2006_07_24_2023_03_22)

dados_A701_H_2006_07_24_2023_03_22['Hora Medicao'] <- as.factor(dados_A701_H_2006_07_24_2023_03_22$'Hora Medicao')

summary(dados_A701_H_2006_07_24_2023_03_22)
summary(dados_A701_H_2006_07_24_2023_03_22$`Hora Medicao`)

#criando dados mensais

dados <- dados_A701_H_2006_07_24_2023_03_22

datas_mes <- dados$"Data Medicao"

summary(datas_mes)
nrow(datas_mes)
length(datas_mes)

datas_mes <- as.character(datas_mes)

for (x in 1: length(datas_mes)){
  if (!is.na(datas_mes[x])){
    print(datas_mes[x])
    data <- strptime(as.character(datas_mes[x]), format = "%Y-%m-%d")
    print(data)
    data <- strftime(data, format = "%Y-%m")
    print(data)
    datas_mes[x] <- data
    print(datas_mes[x])
    #print(x)
  }
}

mes_split <- split(dados, dados$`Data Medicao`)

names = list()
print(colnames(dados)[])
print(colnames(data.frame(mes_split[1])))

for (x in 1:length(data.frame(mes_split[1]))){
  print(data.frame(mes_split[1]))
}



#######################
#######################
dados <- dados_A701_H_2006_07_24_2023_03_22

datas_mes <- dados$"Data Medicao"

summary(datas_mes)
nrow(datas_mes)
length(datas_mes)

datas_mes <- as.character(datas_mes)

dados$`Data Medicao` <- as.factor(datas_mes)
new_data_frame <- data.frame()
lista <- NA
is.na(lista)

mes_split <- split(dados, dados$`Data Medicao`)
summary(data.frame(mes_split[1]))


View(lista)

summary(lista[1][1])


#for (x in 1: nrow(dados_A701_H_2006_07_24_2023_03_22["Hora Medicao"])){
#  if (!is.na(dados_A701_H_2006_07_24_2023_03_22[x, "Hora Medicao"])){
#    dados_A701_H_2006_07_24_2023_03_22[x, "Hora Medicao"] <- as.character(strptime(dados_A701_H_2006_07_24_2023_03_22[x, "Hora Medicao"], "%H%M"))
#    print(x)
#  }
#}


