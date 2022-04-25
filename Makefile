
#	Configuaration

CC := gcc
FILE_TYPE := .c
PYTHON_HEADERS := "/usr/include/python3.9"
GSL_HEADERS := "/usr/include/gsl"

#	C Source Code

SRC_DIR := Source/SVM/C_SRC/
HEADER_DIR := Source/SVM/C_HEADERS

#	Build Folder

OBJ_DIR := bin/

#	Library

LIB_DIR := Source/SVM/
LIB_NAME := c_opt

#	Build Target

BUILD_TARGET := so
BUILD_FLAGS := -O2 -g -Wall -Wextra


LIB := $(LIB_NAME).$(BUILD_TARGET)
LIB_BUILD := $(LIB_DIR)$(LIB)


#	Loading in file locations

SRCS := 										\
	$(wildcard $(SRC_DIR)**/**$(FILE_TYPE)) 	\
	$(wildcard $(SRC_DIR)*$(FILE_TYPE))

OBJS := 														\
	$(patsubst $(SRC_DIR)%$(FILE_TYPE), $(OBJ_DIR)%.o, $(SRCS))


#	Handling automatic dependency tracking

DEPS := $(patsubst %.o, %.d, $(OBJS))

-include $(DEPS)

DEP_FLAGS = -MMD -MF $(@:.o=.d)


build: $(OBJS)
	@echo [INFO] Creating Shared Library [$(BUILD_TARGET)] ...
	@$(CC) -fPIC -shared -o $(LIB_BUILD) $^ -lm -lgsl
	@echo [INFO] [$(LIB)] Created!

$(OBJ_DIR)%.o: $(SRC_DIR)%$(FILE_TYPE)
	@echo [CC] $<
	@mkdir -p $(@D)
	@$(CC) -fPIC $< -c -o $@ $(BUILD_FLAGS) $(DEP_FLAGS) -I$(PYTHON_HEADERS) -I$(GSL_HEADERS) -I$(HEADER_DIR)


.PHONEY: clean
clean:
	@rm -rf $(OBJ_DIR)
	@rm -rf $(DEPS)
	@rm $(LIB_BUILD)