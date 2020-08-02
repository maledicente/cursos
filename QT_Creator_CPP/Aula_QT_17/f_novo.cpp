#include "f_novo.h"
#include "ui_f_novo.h"

F_Novo::F_Novo(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::F_Novo)
{
    ui->setupUi(this);
}

F_Novo::~F_Novo()
{
    delete ui;
}
