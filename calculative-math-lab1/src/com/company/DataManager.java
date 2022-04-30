package com.company;

import java.io.*;

public class DataManager {
    private int typeRead = 0;
    private int matrixOrder;
    private double[][] matrix;
    private final GaussMatrixCalculator gaussMatrixCalculator;

    public DataManager(){
        gaussMatrixCalculator = new GaussMatrixCalculator();
    }

    public void run(){
        while (true) {
            System.out.println("Введите 1, если хотите ввести систему в консоль \nИли 2, если считать из файла");

            while (true){
                try {
                    typeRead = Integer.parseInt(Utils.getScanner().nextLine());
                }catch (Exception ignored){
                }
                if ( typeRead == 1){
                    if (readFromCommandLine()) solveMatrix();
                    break;
                }else if(typeRead == 2){
                    if(readFromFile()) solveMatrix();
                    break;
                }
                System.out.println("Такого варианта нет");
            }
        }

    }

    public void solveMatrix(){
        gaussMatrixCalculator.calculateMatrix(matrix,matrixOrder);
    }

    public boolean readFromCommandLine(){
        System.out.println("Введите порядок матрицы:");
        matrixOrder = Integer.parseInt(Utils.getScanner().nextLine());
        if (matrixOrder<=0 || matrixOrder>20){
            System.out.println("Порядок матрицы должен быть в диапазоне [1;20]");
            return false;
        }
        matrix = new double[matrixOrder][matrixOrder+1];
        System.out.println("Введите построчно элементы для каждой строки," +
                " не забудте про столбец свободных коэффициентов");
        String numbers[];
        for (int i = 0; i<matrixOrder; i++){
            numbers = Utils.getScanner().nextLine().trim().split(" +");
            for (int j = 0; j<matrixOrder+1; j++){
                try{
                    matrix[i][j] = Double.parseDouble(numbers[j]);
                }catch (Exception e){
                    System.out.println("Неправильный ввод в строке " + (i+1));
                    return false;
                }
            }
        }
        return true;
    }

    public boolean readFromFile(){
        System.out.println("Введите путь к файлу:");
        String path = Utils.getScanner().nextLine();
        String numbers[];
        try(Reader reader = new FileReader(path)) {
            BufferedReader bufferedReader = new BufferedReader(reader);
            if (bufferedReader.ready()){
                numbers= bufferedReader.readLine().trim().split(" +");
                if (numbers.length!=1){
                    System.out.println("В 1 строке файла должно быть одно число, порядок матрицы");
                    return false;
                }else{
                    matrixOrder= Integer.parseInt(numbers[0]);
                }
            }
            matrix = new double[matrixOrder][matrixOrder+1];
            int i =0;
            while (bufferedReader.ready() && i<matrixOrder){
                numbers= bufferedReader.readLine().trim().split(" +");
                for (int j = 0; j<matrixOrder+1; j++){
                    try{
                        matrix[i][j] = Double.parseDouble(numbers[j]);
                    }catch (Exception e){
                        System.out.println("Неправильный ввод в строке " + (i+1));
                        return false;
                    }
                }
                i++;
            }
            reader.close();
            bufferedReader.close();
        } catch (FileNotFoundException e) {
            System.out.println("Файл не найден");
        } catch (IOException e) {
            e.printStackTrace();
        }
        return true;
    }

}
