#include "gtest/gtest.h"

#include "pb.h"

TEST(TestPlayBook, PlayBookFunctionReturns0) {
    EXPECT_EQ(pb(), 0);
}
