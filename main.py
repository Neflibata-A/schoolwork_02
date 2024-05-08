#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define CARDS_COUNT 54
#define M 5 // 报数到M时出牌
#define MAX_A_CARDS 5 // 记录打出的A牌的数量

typedef struct Node {
    char card[4];
    struct Node *next;
} Node;

// 初始化栈
void initStack(Node **stack) {
    *stack = NULL;
}

// 压栈操作
void push(Node **stack, char *card) {
    Node *newNode = (Node *)malloc(sizeof(Node));
    strcpy(newNode->card, card);
    newNode->next = *stack;
    *stack = newNode;
}

// 弹栈操作
char *pop(Node **stack) {
    if (*stack == NULL) {
        return NULL;
    }
    Node *temp = *stack;
    *stack = (*stack)->next;
    char *card = strdup(temp->card); // 复制牌面字符串
    free(temp);
    return card;
}
// 创建并初始化顺序表
void createDeck(char deck[][4]) {
    char suits[4] = {'A', 'B', 'C', 'D'};
    char values[] = {'1', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K'};
    int i, j, k = 0;
    for (i = 0; i < 4; ++i) {
        for (j = 0; j < 13; ++j) {
            sprintf(deck[k++], "%c%c", suits[i], values[j]);
        }
    }
    strcpy(deck[52], "XX"); // 小王
    strcpy(deck[53], "YY"); // 大王
}

// 洗牌逻辑
void shuffleDeck(char deck[][4]) {
    srand((unsigned)time(NULL)); // 设置随机种子
    for (int i = CARDS_COUNT - 1; i > 0; --i) {
        int j = rand() % (i + 1);
        char temp[4];
        strcpy(temp, deck[i]);
        strcpy(deck[i], deck[j]);
        strcpy(deck[j], temp);
    }
}
// 报数+出牌逻辑
void playGame(char deck[][4], Node **stack, char (*lastACards)[4]) {
    int current = 0, count = 0, aCardIndex = 0;
    char (*cards)[4] = malloc(CARDS_COUNT * sizeof(char[4]));
    memcpy(cards, deck, sizeof(deck)); // 创建牌数组的副本进行游戏操作
    for (int i = 0; i < MAX_A_CARDS; i++) {
        strcpy(lastACards[i], ""); // 初始化 lastACards 数组
    }

    initStack(stack); // 初始化栈

    while (count != CARDS_COUNT - 1) {
        for (int i = 0; i < M - 1; i++) {
            current = (current + 1) % CARDS_COUNT;
        }
        char cardToPlay[4];
        strcpy(cardToPlay, cards[current]);
        if (cards[current][0] == 'A') {
            strcpy(lastACards[aCardIndex++], cardToPlay);
        }
        push(stack, cardToPlay);
        memmove(&cards[current], &cards[current + 1], (CARDS_COUNT - current - 1) * sizeof(cards[0]));
        current = 0;
        count++;
    }

    // 弹出栈中剩余的牌，直到只剩一张牌
    while (*stack != NULL) {
        pop(stack);
    }

    printf("The last card is: %s\n", cards[0]);
    for (int i = 0; i < aCardIndex; i++) {
        printf("Last A card: %s\n", lastACards[i]);
    }

    free(cards); // 释放动态分配的牌数组
}
int main() {
    char deck[CARDS_COUNT][4];
    char lastACards[MAX_A_CARDS][4];

    // 初始化 lastACards 数组
    for (int i = 0; i < MAX_A_CARDS; i++) {
        lastACards[i][0] = '\0'; // 设置为空字符串
    }

    Node *stack = NULL;
    createDeck(deck);
    shuffleDeck(deck);
    playGame(deck, &stack, lastACards);

    // 释放栈内存
    while (stack != NULL) {
        Node *temp = stack;
        stack = stack->next;
        free(temp);
    }

    // 打印最后打出的A牌
    printf("The last A cards are:\n");
    for (int i = 0; i < MAX_A_CARDS; i++) {
        if (lastACards[i][0] != '\0') { // 如果这张卡牌被打出
            printf("%s\n", lastACards[i]);
        }
    }

    return 0;
}