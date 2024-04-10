// generated from rosidl_generator_c/resource/idl__description.c.em
// with input from drive_base_msgs:msg/CommandStatus.idl
// generated code does not contain a copyright notice

#include "drive_base_msgs/msg/detail/command_status__functions.h"

ROSIDL_GENERATOR_C_PUBLIC_drive_base_msgs
const rosidl_type_hash_t *
drive_base_msgs__msg__CommandStatus__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0x67, 0x52, 0x04, 0xbd, 0xfd, 0x4c, 0x98, 0x59,
      0xb0, 0xcb, 0x8a, 0xb6, 0x02, 0xa7, 0x8d, 0xc4,
      0x61, 0x3e, 0x13, 0x0e, 0xd5, 0xc9, 0x04, 0xb9,
      0x48, 0x31, 0x4a, 0x5e, 0x95, 0x05, 0x5d, 0xab,
    }};
  return &hash;
}

#include <assert.h>
#include <string.h>

// Include directives for referenced types
#include "builtin_interfaces/msg/detail/time__functions.h"
#include "drive_base_msgs/msg/detail/command_header__functions.h"

// Hashes for external referenced types
#ifndef NDEBUG
static const rosidl_type_hash_t builtin_interfaces__msg__Time__EXPECTED_HASH = {1, {
    0xb1, 0x06, 0x23, 0x5e, 0x25, 0xa4, 0xc5, 0xed,
    0x35, 0x09, 0x8a, 0xa0, 0xa6, 0x1a, 0x3e, 0xe9,
    0xc9, 0xb1, 0x8d, 0x19, 0x7f, 0x39, 0x8b, 0x0e,
    0x42, 0x06, 0xce, 0xa9, 0xac, 0xf9, 0xc1, 0x97,
  }};
static const rosidl_type_hash_t drive_base_msgs__msg__CommandHeader__EXPECTED_HASH = {1, {
    0x8a, 0x99, 0x46, 0x44, 0x11, 0x09, 0x1d, 0x30,
    0xec, 0x26, 0xe2, 0x1c, 0x63, 0x39, 0x28, 0x60,
    0x6b, 0xbd, 0x6c, 0x0c, 0x30, 0x5b, 0xe5, 0xd3,
    0x3f, 0x76, 0x75, 0xa3, 0xec, 0x5d, 0x14, 0x76,
  }};
#endif

static char drive_base_msgs__msg__CommandStatus__TYPE_NAME[] = "drive_base_msgs/msg/CommandStatus";
static char builtin_interfaces__msg__Time__TYPE_NAME[] = "builtin_interfaces/msg/Time";
static char drive_base_msgs__msg__CommandHeader__TYPE_NAME[] = "drive_base_msgs/msg/CommandHeader";

// Define type names, field names, and default values
static char drive_base_msgs__msg__CommandStatus__FIELD_NAME__stamp[] = "stamp";
static char drive_base_msgs__msg__CommandStatus__FIELD_NAME__cmd_header[] = "cmd_header";
static char drive_base_msgs__msg__CommandStatus__FIELD_NAME__status[] = "status";

static rosidl_runtime_c__type_description__Field drive_base_msgs__msg__CommandStatus__FIELDS[] = {
  {
    {drive_base_msgs__msg__CommandStatus__FIELD_NAME__stamp, 5, 5},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE,
      0,
      0,
      {builtin_interfaces__msg__Time__TYPE_NAME, 27, 27},
    },
    {NULL, 0, 0},
  },
  {
    {drive_base_msgs__msg__CommandStatus__FIELD_NAME__cmd_header, 10, 10},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE,
      0,
      0,
      {drive_base_msgs__msg__CommandHeader__TYPE_NAME, 33, 33},
    },
    {NULL, 0, 0},
  },
  {
    {drive_base_msgs__msg__CommandStatus__FIELD_NAME__status, 6, 6},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_UINT8,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
};

static rosidl_runtime_c__type_description__IndividualTypeDescription drive_base_msgs__msg__CommandStatus__REFERENCED_TYPE_DESCRIPTIONS[] = {
  {
    {builtin_interfaces__msg__Time__TYPE_NAME, 27, 27},
    {NULL, 0, 0},
  },
  {
    {drive_base_msgs__msg__CommandHeader__TYPE_NAME, 33, 33},
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
drive_base_msgs__msg__CommandStatus__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {drive_base_msgs__msg__CommandStatus__TYPE_NAME, 33, 33},
      {drive_base_msgs__msg__CommandStatus__FIELDS, 3, 3},
    },
    {drive_base_msgs__msg__CommandStatus__REFERENCED_TYPE_DESCRIPTIONS, 2, 2},
  };
  if (!constructed) {
    assert(0 == memcmp(&builtin_interfaces__msg__Time__EXPECTED_HASH, builtin_interfaces__msg__Time__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[0].fields = builtin_interfaces__msg__Time__get_type_description(NULL)->type_description.fields;
    assert(0 == memcmp(&drive_base_msgs__msg__CommandHeader__EXPECTED_HASH, drive_base_msgs__msg__CommandHeader__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[1].fields = drive_base_msgs__msg__CommandHeader__get_type_description(NULL)->type_description.fields;
    constructed = true;
  }
  return &description;
}

static char toplevel_type_raw_source[] =
  "# command has been accepted\n"
  "uint8 OK = 0\n"
  "# the command contained requests that exceed the capabilities of the system\n"
  "# e.g., the command speed was too high\n"
  "# NOTE: The system will still attempt to perform as best it can\n"
  "uint8 CAPABILITIES_EXCEEDED = 1\n"
  "# the command contained invalid values, and the system will not attempt\n"
  "# to perform it\n"
  "uint8 INVALID = 2\n"
  "# the command cannot be executed because the system has insufficient power to operate\n"
  "uint8 POWER_INSUFFICIENT = 3\n"
  "# the system is currently inoperational for an unspecified reason\n"
  "# it expects to be able to recover\n"
  "uint8 TEMPORARY_FAILURE = 4\n"
  "# the system is inoperational indefinitely\n"
  "uint8 SYSTEM_FAILURE = 5\n"
  "\n"
  "\n"
  "# timestamp of this message\n"
  "builtin_interfaces/Time stamp\n"
  "# command this pertains to\n"
  "drive_base_msgs/CommandHeader cmd_header\n"
  "# result of the command\n"
  "uint8 status";

static char msg_encoding[] = "msg";

// Define all individual source functions

const rosidl_runtime_c__type_description__TypeSource *
drive_base_msgs__msg__CommandStatus__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {drive_base_msgs__msg__CommandStatus__TYPE_NAME, 33, 33},
    {msg_encoding, 3, 3},
    {toplevel_type_raw_source, 834, 834},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
drive_base_msgs__msg__CommandStatus__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[3];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 3, 3};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *drive_base_msgs__msg__CommandStatus__get_individual_type_description_source(NULL),
    sources[1] = *builtin_interfaces__msg__Time__get_individual_type_description_source(NULL);
    sources[2] = *drive_base_msgs__msg__CommandHeader__get_individual_type_description_source(NULL);
    constructed = true;
  }
  return &source_sequence;
}
