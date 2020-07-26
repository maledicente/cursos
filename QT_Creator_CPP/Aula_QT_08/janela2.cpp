#include "janela2.h"
#include "ui_janela2.h"

Janela2::Janela2(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::Janela2)
{
    ui->setupUi(this);
}

Janela2::~Janela2()
{
    delete ui;
}
