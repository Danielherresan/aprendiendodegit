from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import export_graphviz
import graphviz
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
import matplotlib.pyplot as plt
import numpy as np
iris = load_iris()
X_train,X_test,y_train,y_test=train_test_split(iris['data'],iris['target'])
arbol=DecisionTreeClassifier()
arbol.fit(X_train,y_train)
print(arbol.score(X_test,y_test))
print(arbol.score(X_train,y_train))
export_graphviz(arbol,out_file='arbol.dot',class_names=iris.target_names,
                feature_names=iris.feature_names,impurity=False,filled=True)
#graficaaaaaaaaaaaaarrrrrrrrrrrrrrr
with open('arbol.dot') as f:
    dot_graph=f.read()
graphviz.Source(dot_graph).view()
caract=iris.data.shape[1]
plt.barh(range(caract),arbol.feature_importances_)
plt.yticks(np.arange(caract),iris.feature_names)
plt.xlabel('importancia de las caracteristicas')
plt.ylabel('Caracteristicas')
plt.show()
arbol=DecisionTreeClassifier(max_depth=3)
arbol.fit(X_train,y_train)
print(arbol.score(X_test,y_test))
print(arbol.score(X_train,y_train))
n_classes=3
plot_colors='bry'
plot_step=0.02
for pairidx, pair in enumerate([[0,1],[0,2],[0,3],[1,2],[1,3],[2,3]]):
    x=iris.data[:,pair]
    y=iris.target
    clf=DecisionTreeClassifier().fit(x,y)
    plt.subplot(2,3,pairidx+1)
    x_min,x_max=x[:,0].min()-1,x[:,0].max()+1
    y_min,y_max=x[:,1].min()-1,x[:,1].max()+1
    xx,yy=np.meshgrid(np.arange(x_min,x_max,plot_step),
                      np.arange(y_min,y_max,plot_step))
    Z=clf.predict(np.c_[xx.ravel(),yy.ravel()])
    Z=Z.reshape(xx.shape)
    cs=plt.contourf(xx,yy,Z,cmpa=plt.cm.Paired)
    plt.xlabel(iris.feature_names[pair[0]])
    plt.ylabel(iris.feature_names[pair[1]])
    plt.axis('tight')
    #graficando los puntos de entrenamiento
    for i, color in zip(range(n_classes),plot_colors):
        idx=np.where(y==i)
        plt.scatter(x[idx,0],x[idx,1], c=color, label=iris.target_names[i],
                    cmap=plt.cm.Paired)
    plt.axis('tight')
plt.suptitle('Ejemplos de clasificador de arboles')
plt.legend()
plt.show()




