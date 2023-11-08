from sklearn.datasets import load_iris, fetch_kddcup99
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text, plot_tree
from sklearn.svm import SVC

################## Pré-processamento ##################
# Coleta e intregração
iris = load_iris()
caracteristicas = iris.data
rotulos = iris.target
print("Características:\n", caracteristicas[:2])
print("Rótulos:\n", rotulos[:2])

# Partição de dados
carac_treino, carac_teste, rot_treino, rot_teste = train_test_split(caracteristicas, rotulos)

################## Mineração ##################
######### ------ Arvore de Decisão ----- ######

arvore = DecisionTreeClassifier(max_depth=2)
arvore.fit(X=carac_treino, y=rot_treino)

rot_previsao = arvore.predict(carac_teste)
precisao_arvore = accuracy_score(rot_teste, rot_previsao)

######## ----- Máquina de vetor suporte ----- ########
clf = SVC()
clf.fit(X=carac_treino, y=rot_treino)
rot_previsao_svm = clf.predict(carac_teste)
precisao_svm = accuracy_score(rot_teste, rot_previsao_svm)

################## Pós-processamento ##################
print('Precisão Árvore de Decisão:', round(precisao_arvore, 5))
print('Precisão SVM:', round(precisao_svm, 5))

r = export_text(arvore, feature_names=iris['feature_names'])
print('Estrutura da árvore')
print(r)