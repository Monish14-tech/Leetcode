import java.util.*;

class Solution {

    public String getPermutation(int n, int k) {

        List<Integer> numbers =
                new ArrayList<>();

        int[] fact =
                new int[n + 1];

        fact[0] = 1;

        for(int i = 1; i <= n; i++) {

            fact[i] =
                    fact[i - 1] * i;

            numbers.add(i);
        }

        k--;

        StringBuilder result =
                new StringBuilder();

        for(int i = n; i >= 1; i--) {

            int blockSize =
                    fact[i - 1];

            int index =
                    k / blockSize;

            result.append(
                    numbers.get(index)
            );

            numbers.remove(index);

            k %= blockSize;
        }

        return result.toString();
    }
}