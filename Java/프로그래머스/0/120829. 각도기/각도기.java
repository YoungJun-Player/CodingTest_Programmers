class Solution {
    public int solution(int angle) {
        if (0 < angle && angle < 90) {
            return 1;
        }
        if (angle == 90) {
            return 2;
        }
        if (90 < angle && angle < 180) {
            return 3;
        }
        if (angle == 180) {
            return 4;
        }
        // 기본값 반환 (예외 처리)
        return 0; // 또는 다른 적절한 값을 반환
    }
}