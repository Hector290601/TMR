// generated from rosidl_generator_c/resource/idl__description.c.em
// with input from drive_base_msgs:msg/TRVCommand.idl
// generated code does not contain a copyright notice

#include "drive_base_msgs/msg/detail/trv_command__functions.h"

ROSIDL_GENERATOR_C_PUBLIC_drive_base_msgs
const rosidl_type_hash_t *
drive_base_msgs__msg__TRVCommand__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0x2f, 0x54, 0x3e, 0x1f, 0x5b, 0xf0, 0x47, 0x89,
      0xdc, 0x8a, 0x5f, 0xba, 0x01, 0xde, 0x78, 0x26,
      0xc4, 0xdf, 0x61, 0xff, 0x94, 0xd0, 0xf2, 0xb3,
      0x39, 0x32, 0x0c, 0xfe, 0xbb, 0xc2, 0xe4, 0xf4,
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

static char drive_base_msgs__msg__TRVCommand__TYPE_NAME[] = "drive_base_msgs/msg/TRVCommand";
static char builtin_interfaces__msg__Time__TYPE_NAME[] = "builtin_interfaces/msg/Time";
static char drive_base_msgs__msg__CommandHeader__TYPE_NAME[] = "drive_base_msgs/msg/CommandHeader";

// Define type names, field names, and default values
static char drive_base_msgs__msg__TRVCommand__FIELD_NAME__header[] = "header";
static char drive_base_msgs__msg__TRVCommand__FIELD_NAME__translational_velocity[] = "translational_velocity";
static char drive_base_msgs__msg__TRVCommand__FIELD_NAME__rotational_velocity[] = "rotational_velocity";

static rosidl_runtime_c__type_description__Field drive_base_msgs__msg__TRVCommand__FIELDS[] = {
  {
    {drive_base_msgs__msg__TRVCommand__FIELD_NAME__header, 6, 6},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE,
      0,
      0,
      {drive_base_msgs__msg__CommandHeader__TYPE_NAME, 33, 33},
    },
    {NULL, 0, 0},
  },
  {
    {drive_base_msgs__msg__TRVCommand__FIELD_NAME__translational_velocity, 22, 22},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {drive_base_msgs__msg__TRVCommand__FIELD_NAME__rotational_velocity, 19, 19},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
};

static rosidl_runtime_c__type_description__IndividualTypeDescription drive_base_msgs__msg__TRVCommand__REFERENCED_TYPE_DESCRIPTIONS[] = {
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
drive_base_msgs__msg__TRVCommand__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {drive_base_msgs__msg__TRVCommand__TYPE_NAME, 30, 30},
      {drive_base_msgs__msg__TRVCommand__FIELDS, 3, 3},
    },
    {drive_base_msgs__msg__TRVCommand__REFERENCED_TYPE_DESCRIPTIONS, 2, 2},
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
  "# Command a mobile base by Translational and Rotational Velocity\n"
  "# Primarily intended for differential drive bases.\n"
  "drive_base_msgs/CommandHeader header\n"
  "float32 translational_velocity\n"
  "float32 rotational_velocity";

static char msg_encoding[] = "msg";

// Define all individual source functions

const rosidl_runtime_c__type_description__TypeSource *
drive_base_msgs__msg__TRVCommand__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {drive_base_msgs__msg__TRVCommand__TYPE_NAME, 30, 30},
    {msg_encoding, 3, 3},
    {toplevel_type_raw_source, 212, 212},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
drive_base_msgs__msg__TRVCommand__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[3];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 3, 3};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *drive_base_msgs__msg__TRVCommand__get_individual_type_description_source(NULL),
    sources[1] = *builtin_interfaces__msg__Time__get_individual_type_description_source(NULL);
    sources[2] = *drive_base_msgs__msg__CommandHeader__get_individual_type_description_source(NULL);
    constructed = true;
  }
  return &source_sequence;
}
