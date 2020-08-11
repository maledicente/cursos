#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QDebug>

int cont=0;

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    tempo=new QTimer(this);
    connect(tempo,SIGNAL(timeout()),this,SLOT(minhaFuncao()));
    tempo->start(1000);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::minhaFuncao(){
    cont++;
    qDebug() << "Teste - Timer:" << cont;

}

