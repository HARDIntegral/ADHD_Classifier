# Configuaration
CC := g++
C_FILE_TYPE := .c
CPP_FILE_TYPE := .cpp
SRC_DIR := src/SVM/C_SRC/
HEADER_DIR := src/SVM/C_HEADERS
OBJ_DIR := bin/
LIB_DIR := src/SVM/
LIB_NAME := c_opt
BUILD_TARGET := so
BUILD_FLAGS := -O1 -g -Wall -Wextra

LIB := $(LIB_NAME).$(BUILD_TARGET)
LIB_BUILD := $(LIB_DIR)$(LIB)
# Loading in file locations
SRCS := $(wildcard $(SRC_DIR)**/**$(C_FILE_TYPE)) $(wildcard $(SRC_DIR)*$(C_FILE_TYPE)) $(wildcard $(SRC_DIR)**/**$(CPP_FILE_TYPE)) $(wildcard $(SRC_DIR)*$(CPP_FILE_TYPE))
OBJS := $(patsubst $(SRC_DIR)%$(FILE_TYPE), $(OBJ_DIR)%.o, $(SRCS))
# Handling automatic dependency tracking
DEPS := $(patsubst %.o, %.d, $(OBJS))
-include $(DEPS)
DEP_FLAGS = -MMD -MF $(@:.o=.d)

build: $(OBJS)
	@echo [INFO] Creating Shared Library [$(BUILD_TARGET)] ...
	@$(CC) -fPIC -shared -o $(LIB_BUILD) $^ -lm -lgsl -labsl_base
	@echo [INFO] [$(LIB)] Created!

$(OBJ_DIR)%.o: $(SRC_DIR)%$(FILE_TYPE)
	@echo [CPPC] $<
	@mkdir -p $(@D)
	@$(CC) -fPIC $< -c -o $@ $(BUILD_FLAGS) $(DEP_FLAGS) -I/usr/include/ -I$(HEADER_DIR)

.PHONEY: clean
clean:
	@rm -rf $(OBJ_DIR)
	@rm -rf $(DEPS)
	@rm $(LIB_BUILD)