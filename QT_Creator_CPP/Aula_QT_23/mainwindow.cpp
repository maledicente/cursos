#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QDir>
#include "QMessageBox"

/*QString local="/home/usuario/Documentos/GitHub/cursos/QT_Creator_CPP/Aula_QT_23/";*/

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    QDir unidades;
    foreach (QFileInfo qfi, unidades.drives()) {
        ui->comboBox->addItem(qfi.absoluteFilePath());
    }

}

MainWindow::~MainWindow()
{
    delete ui;
}


void MainWindow::on_comboBox_currentTextChanged(const QString &arg1)
{
    ui->listWidget->clear();
    ui->listWidget->addItem(arg1);
    QDir conteudo(arg1);
    foreach (QFileInfo qfi, conteudo.entryInfoList()) {
        ui->comboBox->addItem(qfi.absoluteFilePath());
        if(qfi.isDir()){
            ui->listWidget->addItem(qfi.absoluteFilePath());
        }
        /*else if(qfi.isFile()){
            ui->listWidget->addItem("Arquivo..:  "+qfi.absoluteFilePath());
        }*/
    }

}

void MainWindow::on_pushButton_clicked()
{
    QString local=ui->listWidget->currentItem()->text();
    /*QMessageBox::about(this,"Teste",local);*/
    QString nome="/"+ui->lineEdit_2->text();
    QDir dir(local+nome);
    if(dir.exists()){
        QMessageBox::about(this,"pasta","Diretorio ja existe");
    }else{
        dir.mkdir(local+nome);
        ui->listWidget->clear();
        ui->listWidget->addItem(ui->comboBox->currentText());
        QDir conteudo(ui->comboBox->currentText());
        foreach (QFileInfo qfi, conteudo.entryInfoList()) {
            ui->comboBox->addItem(qfi.absoluteFilePath());
            if(qfi.isDir()){
                ui->listWidget->addItem(qfi.absoluteFilePath());
            }
        }
    }
    ui->lineEdit_2->clear();
}

void MainWindow::on_pushButton_2_clicked()
{
    QString local=ui->listWidget->currentItem()->text();
    QDir dir(local);
    if(!dir.exists()){
        QMessageBox::about(this,"pasta","Diretorio não existe");
    }else{
        dir.rmdir(local);
        ui->listWidget->clear();
        ui->listWidget->addItem(ui->comboBox->currentText());
        QDir conteudo(ui->comboBox->currentText());
        foreach (QFileInfo qfi, conteudo.entryInfoList()) {
            ui->comboBox->addItem(qfi.absoluteFilePath());
            if(qfi.isDir()){
                ui->listWidget->addItem(qfi.absoluteFilePath());
            }
        }
    }
}
