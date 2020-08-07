#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "QFile"
#include <QTextStream>
#include <QMessageBox>
#include <QFileDialog>

QString local="/home/usuario/Documentos/GitHub/cursos/QT_Creator_CPP/Aula_QT_24/arquivo_txt/";
QString nome="curso.txt";

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}


void MainWindow::on_btn_gravar_clicked()
{
    QFile arquivo(local+nome);
    if(!arquivo.open(QFile::WriteOnly|QFile::Text)){
        QMessageBox::warning(this,"ERRO","Erro ao abrir o arquivo");
    }
    QTextStream saida(&arquivo);
    QString texto=ui->plainTextEdit->toPlainText();
    saida << texto;
    arquivo.flush();
    arquivo.close();
    ui->plainTextEdit->clear();
}

void MainWindow::on_btn_ler_clicked()
{
    QFile arquivo(local+nome);
    if(!arquivo.open(QFile::ReadOnly|QFile::Text)){
        QMessageBox::warning(this,"ERRO","Erro ao abrir o arquivo");
    }
    QTextStream entrada(&arquivo);
    QString texto=entrada.readAll();
    ui->plainTextEdit->setPlainText(texto);
    arquivo.close();
}

void MainWindow::on_pushButton_clicked()
{
    QString filtro= "Todos os arquivos (*.*);; Arquivos de texto (*.txt)";
    QString abrirArquivo=QFileDialog::getOpenFileName(this,"Abrir Arquivos","/home/usuario/Documentos/GitHub/cursos/",filtro);
    QFile arquivo(abrirArquivo);
    if(!arquivo.open(QFile::ReadOnly|QFile::Text)){
        QMessageBox::warning(this,"ERRO","Erro ao abrir o arquivo");

       }
    QTextStream entrada(&arquivo);
    QString texto=entrada.readAll();
    ui->plainTextEdit->setPlainText(texto);
    arquivo.close();
}
