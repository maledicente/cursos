#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "QMessageBox"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    QString cursos[5]={"C++","Qt","PHP","Unity","Javascript"};
    QString icones[5]={":/icons/icons/c++.png",
                       ":/icons/icons/qt.png",
                       ":/icons/icons/php.png",
                       ":/icons/icons/unity.png",
                       ":/icons/icons/javascript.png"};
    for(int i=0;i<5;i++){
        ui->comboBox->addItem(QIcon(icones[i]),cursos[i]);
    }
    /*ui->comboBox->addItem("C++");
      ui->comboBox->addItem("Qt");
      ui->comboBox->addItem("PHP");
      ui->comboBox->addItem("Unity");
      ui->comboBox->addItem("Javascript");
    */
}

MainWindow::~MainWindow()
{
    delete ui;
}


void MainWindow::on_pushButton_clicked()
{
    QMessageBox::about(this,"Cursos",ui->comboBox->currentText());
}
