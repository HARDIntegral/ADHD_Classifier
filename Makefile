# Configuaration
CC := gcc
FILE_TYPE := .c
PYTHON_HEADERS := "/usr/include/python3.9"
NUMPY_HEADERS := "/usr/lib/python3.9/site-packages/numpy/core/include/numpy"
GSL_HEADERS := "/usr/include/gsl"
SRC_DIR := src/SVM/C_SRC/
HEADER_DIR := src/SVM/C_HEADERS
OBJ_DIR := bin/
LIB_DIR := src/SVM/
LIB_NAME := c_opt
BUILD_TARGET := so
BUILD_FLAGS := -O1 -g -Wall -Wextra -fPIC -I$(GSL_HEADERS) -I$(HEADER_DIR) -I$(NUMPY_HEADERS) -I$(PYTHON_HEADERS)

LIB := $(LIB_NAME).$(BUILD_TARGET)
LIB_BUILD := $(LIB_DIR)$(LIB)
# Loading in file locations
SRCS := $(wildcard $(SRC_DIR)**/**$(FILE_TYPE)) $(wildcard $(SRC_DIR)*$(FILE_TYPE))
OBJS := $(patsubst $(SRC_DIR)%$(FILE_TYPE), $(OBJ_DIR)%.o, $(SRCS))
# Handling automatic dependency tracking
DEPS := $(patsubst %.o, %.d, $(OBJS))
-include $(DEPS)
DEP_FLAGS = -MMD -MF $(@:.o=.d)

build: $(OBJS)
	@echo [INFO] Creating Shared Library [$(BUILD_TARGET)] ...
	@$(CC) -shared -o $(LIB_BUILD) $^
	@echo [INFO] [$(LIB)] Created!

$(OBJ_DIR)%.o: $(SRC_DIR)%$(FILE_TYPE)
	@echo [CC] $<
	@mkdir -p $(@D)
	@$(CC) $< -c -o $@ -lz $(BUILD_FLAGS) $(DEP_FLAGS) 

.PHONEY: clean
clean:
	@rm -rf $(OBJ_DIR)
	@rm -rf $(DEPS)
	@rm $(LIB_BUILD)