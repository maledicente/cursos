#ifndef F_NOVO_H
#define F_NOVO_H

#include <QDialog>

namespace Ui {
class F_Novo;
}

class F_Novo : public QDialog
{
    Q_OBJECT

public:
    explicit F_Novo(QWidget *parent = nullptr);
    ~F_Novo();

private:
    Ui::F_Novo *ui;
};

#endif // F_NOVO_H
