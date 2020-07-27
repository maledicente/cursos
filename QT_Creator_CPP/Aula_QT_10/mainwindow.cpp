#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "QPixmap"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    QPixmap logo("/home/usuario/Documentos/GitHub/cursos/QT_Creator_CPP/Aula_QT_10/Pine forest in the mist_xtrafondos.com.jpg");
    ui->label->setPixmap(logo.scaled(600,600,Qt::KeepAspectRatio));
}

MainWindow::~MainWindow()
{
    delete ui;
}


void MainWindow::on_pushButton_clicked()
{
    QPixmap img("/home/usuario/Documentos/GitHub/cursos/QT_Creator_CPP/Aula_QT_10/jakub-kozlowski-final-towers-as.jpg");
    ui->label->setPixmap(img.scaled(600,600,Qt::KeepAspectRatio));
}
