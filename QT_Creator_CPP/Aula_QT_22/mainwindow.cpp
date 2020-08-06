#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QDir>

QString local="/home/usuario/Documentos/GitHub/cursos/QT_Creator_CPP/Aula_QT_22/";

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
    QDir conteudo(arg1);
    foreach (QFileInfo qfi, conteudo.entryInfoList()) {
        ui->comboBox->addItem(qfi.absoluteFilePath());
        if(qfi.isDir()){
            ui->listWidget->addItem("Pasta......:  "+qfi.absoluteFilePath());
        }else if(qfi.isFile()){
            ui->listWidget->addItem("Arquivo..:  "+qfi.absoluteFilePath());
        }
    }

}
