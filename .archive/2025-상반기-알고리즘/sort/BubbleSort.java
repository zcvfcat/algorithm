package sort;

public class BubbleSort {
  public static void main(String[] args) {
    int testSet[] = { 10, 7, 3, 5, 2, 6 };

    for (int i = testSet.length; i > -1; i--) {
      for (int j = 0; j < i - 1; j++) {
        if (testSet[j] > testSet[j + 1]) {
          int temp = testSet[j];
          testSet[j] = testSet[j + 1];
          testSet[j + 1] = temp;
        }
      }
    }

    for (int i = 0; i < testSet.length; i++) {
      System.out.println(testSet[i]);
    }
  }
}
