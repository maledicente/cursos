#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QDateTime>

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    tempo=new QTimer(this);
    connect(tempo,SIGNAL(timeout()),this,SLOT(atualizaRelogio()));
    tempo->start(1000);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::atualizaRelogio(){
    QTime tempoAtual=QTime::currentTime();
    QString tempoTexto=tempoAtual.toString("hh:mm:ss");
    ui->label->setText(tempoTexto);
}

