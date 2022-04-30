package com.company;

public class GaussMatrixCalculator {

    public void calculateMatrix(double[][] matrix, int matrixOrder) {
        double[][] savedMatrix = matrix;
        transformToTriangle(matrix,matrixOrder);
        if (calculateTriangleMatrixDeterminant(matrix,matrixOrder)!=0){
            calculateDiscrepancies(savedMatrix,matrixOrder,calculateUnknowns(matrix,matrixOrder));
        }
    }

    /*Используя метод Гаусса с выбором главного элемента
     по столбцам преобразуем матрицу к триугольному виду*/
    public double[][] transformToTriangle(double[][] matrix, int matrixOrder) {
        for (int matrixOrderIndex = 0; matrixOrderIndex<matrixOrder;matrixOrderIndex++){
            //выбор главного элемента стобца, меняем строки мтарицы местами
            double columnMaxElement=Math.abs(matrix[matrixOrderIndex][matrixOrderIndex]);
            int columnMaxElementIndex = 0;
            boolean isNeedSwab=false;

            //находим индекс строки
            for (int rowIndex=matrixOrderIndex; rowIndex<matrixOrder; rowIndex++){
                //System.out.println("test---------------+\n"+columnMaxElement+"\n"+Math.abs(matrix[matrixOrderIndex][rowIndex]) );
                if (Math.abs(matrix[rowIndex][matrixOrderIndex]) > columnMaxElement) {
                    columnMaxElement = Math.abs(matrix[matrixOrderIndex][rowIndex]);
                    columnMaxElementIndex = rowIndex;
                    isNeedSwab=true;
                }
            }
            //меняем строки местами
            if (isNeedSwab){
                for (int columnIndex = 0; columnIndex < matrixOrder + 1; columnIndex++) {
                    double temp = matrix[matrixOrderIndex][columnIndex];
                    matrix[matrixOrderIndex][columnIndex] = matrix[columnMaxElementIndex][columnIndex];
                    matrix[columnMaxElementIndex][columnIndex] = temp;
                }
                printMatrix("Поменяли местами строки "+(matrixOrderIndex+1)+" и "+(columnMaxElementIndex+1)+":",
                        matrix,matrixOrder);
            }

            /*метод гаусса, прибавляем главную строку умноженную на коэффициент
             для получения нуля в главных элементах строк, которые ниже*/
            for (int rowIndex = matrixOrderIndex;rowIndex<matrixOrder-1;rowIndex++){
                if (matrix[rowIndex+1][matrixOrderIndex]!=0){
                    double coefficient = -(matrix[rowIndex+1][matrixOrderIndex]/matrix[matrixOrderIndex][matrixOrderIndex]);
                    for (int columnIndex=matrixOrderIndex;columnIndex<matrixOrder+1;columnIndex++){
                        matrix[rowIndex+1][columnIndex]+=matrix[matrixOrderIndex][columnIndex]*coefficient;
                    }
                    printMatrix("Строку "+(matrixOrderIndex+1)+" умножили на "
                                    +coefficient+" и прибавили к "+(rowIndex+2)+":",
                            matrix,matrixOrder);
                }

            }
        }
        System.out.println("-----------------------------");
        return matrix;
    }
    //Перемножаем элементы диоганали и получаем определить матрицы
    public double calculateTriangleMatrixDeterminant(double[][] matrix, int matrixOrder){
        double determinant = matrix[0][0];
        System.out.println(determinant);
        for (int matrixOrderIndex = 1; matrixOrderIndex<matrixOrder;matrixOrderIndex++) {
            determinant*=matrix[matrixOrderIndex][matrixOrderIndex];
            System.out.println(matrix[matrixOrderIndex][matrixOrderIndex]);
        }
        if (determinant == 0) {
            System.out.println("Нет решений или их бесконечно много детерсминант = 0");
        } else {
            System.out.println("Детерминант = " + determinant);
        }
        System.out.println("-----------------------------");
        return determinant;
    }

    //Расчитываем неизвестные для треугольной матрицы
    public double[] calculateUnknowns(double[][] matrix, int matrixOrder){
        double[] findVariables=new double[matrixOrder];
        for (int i = matrixOrder-1; i>=0;i--){
            double s =0;
            for (int j = matrixOrder-1; j>=0;j--) {
                s+=matrix[i][j]*findVariables[j];
            }
            findVariables[i]=(matrix[i][matrixOrder]-s)/matrix[i][i];
        }
        for (int i =0; i<matrixOrder;i++){
            System.out.print("x"+(i+1)+" = "+findVariables[i]+" ");
        }
        System.out.println("\n-----------------------------");
        return findVariables;
    }

    /*Невязка это разница между правой и левой частями уравнений,
    при подстановке полученных мет. гаусса ответов*/
    public double[] calculateDiscrepancies(double[][] matrix, int matrixOrder,double[] unknownsVariables){
        double[] discrepancies = new double[matrixOrder];
        System.out.println("Невязки:");
        for (int i=0; i<matrixOrder;i++){
            double sum=0;
            for (int j =0;j<matrixOrder; j++){
                sum+=matrix[i][j]*unknownsVariables[j];
            }
            discrepancies[i]=sum-matrix[i][matrixOrder];
            System.out.println("Уравнение №"+(i+1)+":");
            System.out.println(sum+" - "+matrix[i][matrixOrder]+" = "+ discrepancies[i]);

        }
        System.out.println("=====================================");
        return discrepancies;
    }

    private void printMatrix(String message,double matrix[][],int matrixOrder){
        System.out.println(message);
        for (int i =0;i<matrixOrder;i++){
            for (int j =0;j<matrixOrder+1;j++) {
                System.out.print(String.format("%.2f",matrix[i][j])+" ");
            }
            System.out.print("\n");
        }
    }
}
